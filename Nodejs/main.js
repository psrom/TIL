var http = require('http');
var fs = require('fs');

var app = http.createServer(function(request, response) {
    var varUrl = request.url; // ?id=HTML
    var myURL = new URL('http://localhost:3000' + varUrl); // http://localhost......TML
    var queryData = myURL.searchParams.get('id'); // HTML
    // console.log(myURL);

    var pathname = myURL.pathname;

    if(pathname === "/"){
        if(queryData === null) {

            fs.readdir('./data', function(error, filelist){
                var title = 'Welcome';
                var description = 'Hello, Node.js';
                var list = '<ul>';
                var i = 0;
                while(i < filelist.length) {
                    list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
                    i++;
                }
                list = list + '</ul>';

                var template = `
                    <!doctype html>
                    <html>
                    <head>
                      <title>WEB1 - ${title}</title>
                      <meta charset="utf-8">
                    </head>
                    <body>
                      <h1><a href="/">WEB</a></h1>
                      ${list}
                      <h2>${title}</h2>
                      <p>${description}</p>
                    </body>
                    </html>
                    `;
                    response.writeHead(200);
                    response.end(template);
                });

            } else {
                fs.readdir('./data', function(error, filelist){
                var title = 'Welcome';
                var description = "Hello, Node.js";
                var list = '<ul>';
                var i = 0;
                while(i < filelist.length) {
                    list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
                    i++;
                }
                list = list + '</ul>';
                fs.readFile(`data/${queryData}`, 'utf8', function(err, description){
                    var title = queryData;
                    var template = `
                        <!doctype html>
                        <html>
                        <head>
                          <title>WEB1 - ${title}</title>
                          <meta charset="utf-8">
                        </head>
                        <body>
                          <h1><a href="/">WEB</a></h1>
                          ${list}
                          <h2>${title}</h2>
                          <p>${description}</p>
                        </body>
                        </html>
                        `;
                        response.writeHead(200);
                        response.end(template);
                });
            });
        }
    } else {
        response.writeHead(404);
        response.end('Not found');
    }


});
app.listen(3000);
