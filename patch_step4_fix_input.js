const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

content = content.replace(
    /onfocus="handleNumericFocus\(this\)" onblur="handleNumericBlur\(this\)" oninput="handleNumericInput\(this\)"/g,
    ""
);

fs.writeFileSync('index.html', content);
