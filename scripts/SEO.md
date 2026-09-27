# SEO pentru protocoale.co.uk

Adresa principală este `https://protocoale.co.uk/`, configurată în `mkdocs.yml`
și `config/institution.yml`. Build-ul generează URL-urile canonice, metadatele
Open Graph/Twitter, datele JSON-LD WebSite/WebPage/BreadcrumbList și `robots.txt`.
Navigarea ierarhică vizibilă folosește aceleași pagini ca datele structurate.
`navigation.prune` reduce HTML-ul meniului la ramurile relevante pentru pagina
curentă. Celelalte secțiuni rămân accesibile prin linkuri către paginile lor index.

Descrierile din front matter (`description`) au prioritate. Dacă lipsesc,
`scripts/seo.py` generează descrieri specifice titlului și tipului paginii.
Pentru paginile importante, adaugă descrieri editoriale concise și relevante.
Titlurile și metadatele nu certifică revizuirea sau validitatea clinică.

`robots: noindex, follow` exclude o pagină din sitemap-ul XML și transmite
directiva în HTML. Pagina formularului și pagina 404 nu sunt destinate indexării.
Sitemap-ul folosește numai datele `last_updated` valide, fără date viitoare;
data compilării nu este prezentată ca dată de actualizare editorială.
`docs/javascripts/sitemap.json` este un index separat pentru extensia aplicației.

Verificare locală:

```powershell
python -m pytest tests/test_seo.py tests/test_search_enhancer_index.py -q
python -m mkdocs build
```

După publicare, verifică `https://protocoale.co.uk/robots.txt` și
`https://protocoale.co.uk/sitemap.xml`, apoi trimite sitemap-ul în proprietatea
domeniului din Google Search Console. Redirecționările permanente de pe domeniile
alternative (GitHub Pages / pages.dev), dacă sunt încă publice, se configurează
separat la furnizorul de găzduire; eticheta canonical nu este o redirecționare.

Referințe: [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide),
[Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap),
[BreadcrumbList](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb).
