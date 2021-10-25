/*let height = 5;
let width = (2 * height) - 1;
const abs = (d) => {
    return d < 0 ? -1 * d : d;
}
const printA = () => {
    let n = parseInt(width / 2), i, j;
    for (i = 0; i < height; i++) {
        for (j = 0; j <= width; j++) {
            if (j == n || j == (width - n)
                || (i == parseInt(height / 2) && j > n
                    && j < (width - n)))
                document.write("*");
            else
                document.write("  ");
        }
        document.write(`<br/>`);
        n--;
    }
}

printA();
*/
var number = 0;
            var div = document.getElementById("internal");
            var table = document.createElement("table");
            div.appendChild(table);

            for (var i = 0; i < 7; i++) {

                var rows = document.createElement("tr");
                table.appendChild(rows);

                for (var j = 0; j < 7; j++) {

                    var columns = document.createElement("td");
                    var text = document.createTextNode(number);
                    columns.appendChild(text);
                    rows.appendChild(columns);
                    number++;
                }
            }