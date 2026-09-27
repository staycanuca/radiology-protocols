"""Build-time metadata, linked breadcrumbs and crawl files for the public site."""

from datetime import date, datetime
import gzip
from html import unescape
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urljoin
import xml.etree.ElementTree as ET


_pages = {}
_SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def plain_text(value):
    return " ".join(unescape(re.sub(r"<[^>]+>", "", str(value or ""))).split())


def description_for(page, config):
    """Honor editorial descriptions; fall back to page-specific, nonclinical copy."""
    if page.meta.get("description"):
        return plain_text(page.meta["description"])
    title = plain_text(page.meta.get("title") or page.title)
    if page.file.src_uri == "index.md":
        return config["site_description"]
    if page.meta.get("slug"):
        return f"{title}. Consultă protocolul de examinare și detaliile tehnice în ghidul de radiologie în limba română."
    if page.file.src_uri.endswith("/index.md"):
        return f"{title}: explorează protocoalele și paginile disponibile în ghidul de radiologie în limba română."
    return f"{title}. Informații și resurse din ghidul protocoalelor de radiologie în limba română."


def on_pre_build(config):
    # Hooks persist across live-reload builds.
    _pages.clear()


def on_page_content(html, page, config, files):
    page.meta["description"] = description_for(page, config)
    return html


def on_page_context(context, page, config, nav):
    base = config["site_url"]
    title = plain_text(page.meta.get("title") or page.title)
    # Short branding avoids repeating the long site name on every protocol.
    seo_title = title if page.is_homepage else f"{title} | Protocoale Radiologie"
    robots = str(page.meta.get("robots") or "index, follow, max-image-preview:large")
    by_source = {item.file.src_uri: item for item in nav.pages}
    crumbs = []
    source = PurePosixPath(page.file.src_uri)
    for parent in reversed(source.parents):
        candidate = by_source.get(str(parent / "index.md"))
        if candidate is not None and candidate is not page:
            crumbs.append({"name": plain_text(candidate.meta.get("title") or candidate.title), "path": candidate.url,
                           "url": candidate.canonical_url})
    crumbs.append({"name": title, "path": page.url, "url": page.canonical_url})

    website = {"@type": "WebSite", "@id": base + "#website", "url": base,
               "name": config["site_name"], "inLanguage": "ro"}
    webpage = {"@type": "WebPage", "@id": page.canonical_url + "#webpage",
               "url": page.canonical_url, "name": title,
               "description": page.meta["description"], "inLanguage": "ro",
               "isPartOf": {"@id": website["@id"]}}
    graph = [website, webpage]
    if len(crumbs) > 1:
        breadcrumb_id = page.canonical_url + "#breadcrumb"
        webpage["breadcrumb"] = {"@id": breadcrumb_id}
        graph.append({"@type": "BreadcrumbList", "@id": breadcrumb_id,
                      "itemListElement": [
                          {"@type": "ListItem", "position": i, "name": crumb["name"],
                           "item": crumb["url"]} for i, crumb in enumerate(crumbs, 1)]})
    page.meta["seo"] = {"title": seo_title, "robots": robots, "breadcrumbs": crumbs,
                        "schema": {"@context": "https://schema.org", "@graph": graph}}
    _pages[page.canonical_url] = {
        "noindex": bool({"noindex", "none"} & set(re.split(r"[\s,]+", robots.lower()))),
        "updated": page.meta.get("last_updated"),
    }
    return context


def valid_date(value):
    """Use real editorial dates, never the build time or a future date."""
    try:
        parsed = date.fromisoformat(str(value)[:10])
        return parsed.isoformat() if parsed <= datetime.now().date() else None
    except (ValueError, TypeError):
        return None


def on_post_build(config):
    site = Path(config["site_dir"])
    sitemap = site / "sitemap.xml"
    if sitemap.exists():
        ET.register_namespace("", _SITEMAP_NS)
        tree = ET.parse(sitemap)
        root = tree.getroot()
        for entry in list(root):
            url = entry.findtext(f"{{{_SITEMAP_NS}}}loc")
            meta = _pages.get(url, {})
            if meta.get("noindex"):
                root.remove(entry)
                continue
            for lastmod in entry.findall(f"{{{_SITEMAP_NS}}}lastmod"):
                entry.remove(lastmod)
            updated = valid_date(meta.get("updated"))
            if updated:
                ET.SubElement(entry, f"{{{_SITEMAP_NS}}}lastmod").text = updated
        tree.write(sitemap, encoding="utf-8", xml_declaration=True)
        (site / "sitemap.xml.gz").write_bytes(gzip.compress(sitemap.read_bytes(), mtime=0))
    (site / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: " + urljoin(config["site_url"], "sitemap.xml") + "\n",
        encoding="utf-8",
    )
