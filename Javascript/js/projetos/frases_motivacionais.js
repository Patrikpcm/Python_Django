function geraFraseMotivacional(){

    const frases = ["Se expressarmos gratidão pelo que temos, teremos mais por que expressar gratidão.",
                    "Acorde todas as manhãs com um sorriso. Esta é mais uma oportunidade que você tem para ser feliz. Seja seu próprio motor de ignição. O dia de hoje jamais voltará .... Não o desperdice!",
                    "A vida reserva surpresas maravilhosas para todos aqueles que cultivam a gratidão!",
                    "Lembre-se do seu passado com carinho. Afinal, é por causa dele que você está aqui hoje!",
                    "Sucesso é um esporte coletivo. Demonstre gratidão a todos os que colaboram com suas vitórias.",
                    "Vamos agradecer aos idiotas. Não fosse por eles não faríamos tanto sucesso.",
                    "Lute. Acredite. Conquiste. Perca. Deseje. Espere. Alcance. Invada. Caia. Seja tudo o quiser ser, mas, acima de tudo, seja você sempre."
                    ]
    const numAleatorio = 0;
    const frase = frases[Math.floor(Math.random() * 7)];

    document.getElementById('frase').innerHTML = frase;
}