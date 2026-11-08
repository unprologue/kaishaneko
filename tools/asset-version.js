// Adds ?v=<content hash> to styles.css and script.js in index.html so browsers
// fetch the new files after each deploy instead of reusing a cached copy.
// Run after editing either file: npm run version-assets
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const root = path.join(__dirname, "..");
const pages = ["index.html", "company.html", "legal/tokushoho.html", "legal/privacy.html"]
  .map((page) => path.join(root, page))
  .filter((page) => fs.existsSync(page));

const versions = {};
for (const file of ["styles.css", "script.js"]) {
  const hash = crypto
    .createHash("sha1")
    .update(fs.readFileSync(path.join(root, file)))
    .digest("hex")
    .slice(0, 10);
  versions[file] = hash;
  console.log(`${file}?v=${hash}`);
}

// matches "styles.css", "/styles.css" and their ?v= forms
for (const page of pages) {
  let html = fs.readFileSync(page, "utf8");
  for (const [file, hash] of Object.entries(versions)) {
    const pattern = new RegExp(`(["'])(/?)${file.replace(".", "\\.")}(\\?v=[^"']*)?\\1`, "g");
    if (!pattern.test(html)) throw new Error(`${file} is not referenced in ${path.relative(root, page)}`);
    html = html.replace(pattern, `$1$2${file}?v=${hash}$1`);
  }
  fs.writeFileSync(page, html);
}
