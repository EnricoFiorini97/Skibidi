function ricerca() {
    var input; 
    var filtro;
    var lista;
    var voci;
    var x;
    var i;
    var testo;
      input = document.getElementById("barra-ricerca");
      filtro = input.value.toUpperCase();
      lista = document.getElementById("elenco");
      voci = lista.getElementsByTagName("li");
      for (i = 0; i < voci.length; i++) {
        x = lista.getElementsByTagName("li")[i];
        testo = x.textContent || x.innerText;
        if (testo.toUpperCase().indexOf(filtro) > -1) {
          voci[i].style.display = "";
        } else {
          voci[i].style.display = "none";
        }
      }
    }