
function executar(){
    const obj = document.querySelector('span');
    const classes = obj.classList;
    console.log(classes);
    console.log(classes.length);
    console.log(classes.contains('vermelho'));
    classes.remove('vermelho');
    //classes.add('vermelho'); //adicionar uma classe
    //classes.add('vermelho', 'texto', 'laranja'); //posso adicionar varias classes de uma vez
    //classes.className = ("vermelho texto") //tambem posso modificar a classe diretamente
    classes.toggle("texto"); //alterna entre a classe, remove se existe, adiciona se não.
}