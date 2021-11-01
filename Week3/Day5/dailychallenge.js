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

var div = document.getElementById("internal");
var table = document.createElement("table");
div.appendChild(table);

for (var row = 0; row < 7; row++) {
    var rows = document.createElement("tr");
    table.appendChild(rows)

    for (var col = 0; col < 8; col++) {
        var columns = document.createElement("td");
        if (row===0 && col!==0)  {
            var text = document.createTextNode(col-1);
            columns.appendChild(text);
            rows.appendChild(columns);
        }
    
        else if (col===0 && row!==0) {
            var text = document.createTextNode(row-1);
            columns.appendChild(text);
            rows.appendChild(columns);
}
        else {
            if ((col==2 || col==6)&& row!==1 ){
            var text = document.createTextNode("*");
            columns.appendChild(text);
            rows.appendChild(columns);
            }   
            else if ((row ==1 || row ==3) && (col == 3 || col ==4 || col ==5)){
                var text = document.createTextNode("*");
                columns.appendChild(text);
                rows.appendChild(columns); 
            }
            else {
                var text = document.createTextNode(" ");
                columns.appendChild(text);
                rows.appendChild(columns);
            }

        }
}
}
