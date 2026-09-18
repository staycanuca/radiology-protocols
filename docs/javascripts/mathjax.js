window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  // The CDN script may still be loading when the first page event fires.
  if (typeof window.MathJax.typesetPromise === "function") {
    window.MathJax.typesetPromise().catch(console.error)
  }
})
