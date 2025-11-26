def cell(indent):
    return " " * indent + "<td></td>"

def row(width, indent):
    return (
        " " * indent + "<tr>\n" +
        ( cell(indent + 2) + "\n" ) * width +
        " " * indent + "</tr>"
    )

def table(height, width, indent):
    return (
        " " * indent + "<table>\n" +
        ( row(width, indent + 2) + "\n" ) * height +
        " " * indent + "</table>"
    )

def html():
    return (
        html_head +
        "\n<body>" +
        "\n" + table(100, 100, 0) +
        '\n<script src="cellular.js"></script>' +
        "\n</body>"
    )

html_head = """
<!DOCTYPE html>
<head>
<style>
table {
  border-collapse: collapse;
}
td {
  border: 1px solid rgb(160 160 160);
  padding: 2px 2px;
}
.light {
  background-color: #ff0000;
}
</style>
</head>
"""

if __name__ == "__main__":
    with open("index.html", "w") as f:
        f.write(html())
