function calcularMelhorPreco(){
    //validar campos
    let precoAlcool = document.getElementById("alcool").value
    let precoGasolina = document.getElementById("gasolina").value
    
    if (precoAlcool != ""){
      if(precoGasolina != ""){
        if((precoAlcool/precoGasolina) > 0.7 ){
          //alert("Melhor usar gasolina")
          document.getElementById('resultado').innerHTML = "Melhor utilizar gasolina"
        }
        else{
          //alert("Melhor usar alcool")
          document.getElementById('resultado').innerHTML = "Melhor utilizar álcool"
        }
      }
      else{
        alert("Preencha o campo: Preço da Gasolina")
      }
    }
    else{
      alert("Preencha o campo: Preço do Álcool")
    }
  }