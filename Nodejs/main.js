var http = require('http');
var fs = require('fs');

function templateHTML(title, list, body, control){
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
     ${control}
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
    var qs = require('querystring');
    // console.log(myURL);

    var pathname = myURL.pathname;

    if(pathname === "/"){
        if(queryData === null) {
            fs.readdir('./data', function(error, filelist){
                var title = 'Welcome';
                var description = 'Hello, Node.js';
                var list = templateList(filelist);
                var template = templateHTML(title, list,
                `<h2>${title}</h2>${description}`,
                `<a href="/create">create</a>`
                );
                response.writeHead(200);
                response.end(template);
                })
            } else {
                fs.readdir('./data', function(error, filelist){
                    fs.readFile(`data/${queryData}`, 'utf8', function(err, description){
                        var title = queryData;
                        var list = templateList(filelist);
                        var template = templateHTML(title, list,
                        `<h2>${title}</h2>${description}`,
                        `<a href="/create">create</a>
                        <a href="/update?id=${title}">update</a>
                        <form action="delete_process" method="post">
                            <input type="hidden" name="id" value="${title}">
                            <input type="submit" value="delete">
                        </form>`
                        );
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
        <form action="/create_process" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p>
                <textarea name="description" placeholder="description"></textarea>
            </p>
            <p>
                <input type="submit">
            </p>
        </form>
        `, '');
        response.writeHead(200);
        response.end(template);
        });
    } else if(pathname === '/create_process'){
        var body = '';
        request.on('data', function(data){
            body = body + data;
        });
        request.on('end', function(){
            var post = qs.parse(body);
            var title = post.title;
            var description = post.description;
            fs.writeFile(`data/${title}`, description, 'utf8', function(err){
                response.writeHead(302, {Location: `/?id=${title}`});
                response.end();
            })
        });
    } else if(pathname === '/update'){
        fs.readdir('./data', function(error, filelist){
            fs.readFile(`data/${queryData}`, 'utf8', function(err, description){
                var title = queryData;
                var list = templateList(filelist);
                var template = templateHTML(title, list,
                    `
                    <form action="/update_process" method="post">
                        <input type="hidden" name="id" value="${title}">
                        <p><input type="text" name="title" placeholder="title" value="${title}"></p>
                        <p>
                            <textarea name="description" placeholder="description">${description}</textarea>
                        </p>
                        <p>
                            <input type="submit">
                        </p>
                    </form>
                    `,
                    `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`
                );
                response.writeHead(200);
                response.end(template);
            });
        });
    } else if(pathname === '/update_process'){
        var body = '';
        request.on('data', function(data){
            body = body + data;
        });
        request.on('end', function(){
            var post = qs.parse(body);
            var id = post.id;
            var title = post.title;
            var description = post.description;
            fs.rename(`data/${id}`, `data/${title}`, function(error){
                fs.writeFile(`data/${title}`, description, 'utf8', function(err){
                    response.writeHead(302, {Location: `/?id=${title}`});
                    response.end();
                })
            })
            console.log(post);
        });

    } else if(pathname === '/delete_process'){
              var body = '';
              request.on('data', function(data){
                  body = body + data;
              });
              request.on('end', function(){
                  var post = qs.parse(body);
                  var id = post.id;
                  fs.unlink(`data/${id}`, function(error){
                    response.writeHead(302, {Location: `/`});
                    response.end();
                  })

              });

          }else {
        response.writeHead(404);
        response.end('Not found');
    }

});
app.listen(3000);
