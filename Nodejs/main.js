var http = require('http');
var fs = require('fs');

function templateHTML(title, list, body){
    return `
   <!doctype html>
   <html>
   <head>
     <title>WEB1 - ${title}</title>
     <meta charset="utf-8">
   </head>
   <body>
     <h1><a href="/">WEB</a></h1>
     ${list}
     <a href="/create">create</a>
     ${body}
   </body>
   </html>
   `;
}

function templateList(filelist){
    var list = '<ul>';
    var i = 0;
    while(i < filelist.length) {
        list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
        i++;
    }
    list = list + '</ul>';
    return list;
}

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
                var list = templateList(filelist);
                var template = templateHTML(title, list, `<h2>${title}</h2>${description}`);
                response.writeHead(200);
                response.end(template);
                })
            } else {
                fs.readdir('./data', function(error, filelist){
                    fs.readFile(`data/${queryData}`, 'utf8', function(err, description){
                        var title = queryData;
                        var list = templateList(filelist);
                        var template = templateHTML(title, list, `<h2>${title}</h2>${description}`);
                        response.writeHead(200);
                        response.end(template);
                });
            });
        }
    } else if(pathname === '/create'){
    fs.readdir('./data', function(error, filelist){
        var title = 'WEB - create';
        var list = templateList(filelist);
        var template = templateHTML(title, list, `
        <form action="http://localhost:3000/process_create" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p>
                <textarea name="description" placeholder="description"></textarea>
            </p>
            <p>
                <input type="submit">
            </p>
        </form>
        `);
        response.writeHead(200);
        response.end(template);
        })
    }
    else {
        response.writeHead(404);
        response.end('Not found');
    }


});
app.listen(3000);
