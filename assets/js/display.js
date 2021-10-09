$(document).ready(function () {
    $('#disptable').DataTable( {
        columns: [
            {title: "Name"},
            {title: "Blood Group"},
            {title: "Date of Birth"},
            {title: "Email ID"},
            {title: "Contact"},
        ]
    });
});