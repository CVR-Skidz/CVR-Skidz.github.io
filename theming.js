var storage = window.localStorage;

document.getElementById("theme").addEventListener("click", toggle, false);

if(storage.getItem("theme") === "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
}
else {
    storage.setItem("theme", "light");
}

function toggle() {
    if(storage.getItem("theme") === "light") {
         document.querySelector("meta[name=theme-color]").setAttribute("content", "#000000");
        document.documentElement.setAttribute("data-theme", "dark");
        storage.setItem("theme", "dark");
    }
    else {
         document.querySelector("meta[name=theme-color]").setAttribute("content", "#ffffff");
        document.documentElement.setAttribute("data-theme", "light");
        storage.setItem("theme", "light");
    }
}