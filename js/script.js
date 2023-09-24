document.querySelector(".button").addEventListener("click", loader);

function loader() {
    document.querySelector(".preloader").classList.remove('hide');
    document.querySelector(".button").classList.add('hide');
}

FReader = new FileReader();
let check = 1;
check_fun();
// событие, когда файл загрузится
FReader.onload = function(e) {
    document.querySelector("#preview-result").src = e.target.result;
    check = 0;
    check_fun();
};
 
// выполнение функции при выборки файла
document.querySelector("input").addEventListener("change", loadImageFile);
 
// функция выборки файла
function loadImageFile() {
    var file = document.querySelector("input").files[0];
    FReader.readAsDataURL(file);
}

function check_fun() {
    if (check == 0) {
        document.querySelector('.preview').classList.add('visible');
        document.querySelector('.result').classList.remove('visible');
    }
    else {
        document.querySelector('.result').classList.add('visible');
        document.querySelector('.preview').classList.remove('visible');
    }
}