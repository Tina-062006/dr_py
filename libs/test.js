console.log(Object.keys(a))

console.log(typeof(a.init))

a.replace('export default','export const default_drpy=')


import aa from "./a.js"
console.log(Object.keys(aa));
console.log(typeof(aa));
console.log(typeof(aa.init));


function aa(parse){
    print('parse前:'+parse);
    let option = undefined;
    if (parse.startsWith('body&&')) {
        parse = parse.substr(6);
    }
    if (parse.indexOf('&&') > -1) {
        let sp = parse.split('&&');
        option = sp[sp.length - 1];
        sp.splice(sp.length - 1);
        sp.forEach((it,idex)=>{
            if(/:eq\((.*?)\)/.test(it)){
                let pos = parseInt(it.match(/:eq\((.*?)\)/)[1]);
                if(pos >= 0 ){ // jsoup的eq 正整数从1开始
                    it = it.replace(/:eq\((.*?)\)/,`:eq(${pos+1})`);
                    sp[idex] = it;
                }
            }
        });
        parse = sp.join(' ');
    }
    if (option) {
        parse = parse + '&&' + option;
    }
    print('parse后:'+parse);
}