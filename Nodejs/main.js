var http = require('http');
var fs = require('fs');

var app = http.createServer(function(request, response) {
    var varUrl = request.url; // ?id=HTML
    var myURL = new URL('http://localhost:3000' + varUrl); // http://localhost......TML
    var queryData = myURL.searchParams.get('id'); // HTML
    var title = queryData;

    // console.log(myURL);

    var pathname = myURL.pathname;

    if(pathname === "/"){
        fs.readFile(`data/${queryData}`, 'utf8', function(err, description){
            var template = `
                <!doctype html>
                <html>
                <head>
                  <title>WEB1 - ${title}</title>
                  <meta charset="utf-8">
                </head>
                <body>
                  <h1><a href="/">WEB</a></h1>
                  <ul>
                    <li><a href="/?id=HTML">HTML</a></li>
                    <li><a href="/?id=CSS">CSS</a></li>
                    <li><a href="/?id=JavaScript">JavaScript</a></li>
                  </ul>
                  <h2>${title}</h2>
                  <p>${description}</p>
                </body>
                </html>
                `;
                response.writeHead(200);
                response.end(template);
        });
    } else {
        response.writeHead(404);
        response.end('Not found');
    }


});
app.listen(3000);
