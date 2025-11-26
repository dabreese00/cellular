function getPosition(x, y) {
    table = document.querySelector("table");
    row = table.rows[y];
    return row.children[x];
}

function lightUp(element) {
    element.className = "light";
}

lightUp(getPosition(4,6));
