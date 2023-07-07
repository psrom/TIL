var memberArray = ['egoing', 'graphittie', 'leezhce'];
console.log("memberArray[2]", memberArray[2]);

var memberObject = {
    manager:'egoing', // 'manager'라고 작성해도 됨
    developer: 'graphittie',
    designer: 'leezhce'
}
memberObject.designer = 'leezche';
console.log("memberObject.designer", memberObject.designer);
console.log("memberObject['designer']", memberObject['designer']);
delete memberObject.manager
console.log('after delete memberObject.manager', memberObject.manager);
