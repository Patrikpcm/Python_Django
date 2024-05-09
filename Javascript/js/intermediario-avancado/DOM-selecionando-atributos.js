const img = document.querySelector('#imagem');
const link = document.querySelector('#link');

console.log(img);
console.log(img.getAttribute('src'));
console.log(img.getAttribute('width'));
console.log(img['src']);
console.log(img.src);

function trocarImagem(){
    let img = document.querySelector('#imagem');
    if (img.src == "file:///home/tite/Documentos/Cursos/Python_Django/Javascript/js/intermediario-avancado/arquivos/img/celular.png")
        img.src = "file:///home/tite/Documentos/Cursos/Python_Django/Javascript/js/intermediario-avancado/arquivos/img/grafico.png";
    else
        img.src = "file:///home/tite/Documentos/Cursos/Python_Django/Javascript/js/intermediario-avancado/arquivos/img/celular.png"
}
