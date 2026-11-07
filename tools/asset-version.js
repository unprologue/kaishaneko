// Adds ?v=<content hash> to styles.css and script.js in index.html so browsers
// fetch the new files after each deploy instead of reusing a cached copy.
// Run after editing either file: npm run version-assets
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const root = path.join(__dirname, "..");
const htmlPath = path.join(root, "index.html");
let html = fs.readFileSync(htmlPath, "utf8");

for (const file of ["styles.css", "script.js"]) {
  const hash = crypto
    .createHash("sha1")
    .update(fs.readFileSync(path.join(root, file)))
    .digest("hex")
    .slice(0, 10);
  const pattern = new RegExp(`(["'])${file.replace(".", "\\.")}(\\?v=[^"']*)?\\1`, "g");
  if (!pattern.test(html)) throw new Error(`${file} is not referenced in index.html`);
  html = html.replace(pattern, `$1${file}?v=${hash}$1`);
  console.log(`${file}?v=${hash}`);
}

fs.writeFileSync(htmlPath, html);
