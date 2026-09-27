Local AI rendering dependencies

- DOMPurify 3.4.16 — https://github.com/cure53/DOMPurify (DOMPurify-LICENSE)
- Marked 18.0.14 — https://github.com/markedjs/marked (Marked-LICENSE)

Loaded only when rendering an assistant answer. Markdown must pass through DOMPurify before insertion into the page. Provider SDKs are loaded separately, only after explicit provider use.
