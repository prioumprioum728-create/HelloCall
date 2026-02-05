const fs = require("fs");

const indexHtml = `
<!DOCTYPE html>
<html>
<head>
  <title>HelloCall Website</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>🚀 Welcome to your Website</h1>
  <p>This site was created using the HelloCall GitHub Action.</p>
</body>
</html>
`;

const styleCss = `
body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  text-align: center;
  padding: 40px;
}
h1 {
  color: #2b6cb0;
}
`;

fs.writeFileSync("index.html", indexHtml);
fs.writeFileSync("style.css", styleCss);

console.log("✅ Website files created successfully!");
