document.addEventListener("DOMContentLoaded", function () {
    fetch("file.csv")
        .then(response => response.text())
        .then(csvText => {
            Papa.parse(csvText, {
                header: true,
                skipEmptyLines: true,
                complete: function(results) {
                    const tbody = document.querySelector("table tbody");
                    results.data.forEach(row => {
                        const tr = document.createElement("tr");
                        tr.innerHTML = `
                            <td class="px-6 py-4">${row.Titolo || ""}</td>
                            <td class="px-6 py-4">${row.Nome || ""}</td>
                            <td class="px-6 py-4">${row.Cognome || ""}</td>
                            <td class="px-6 py-4">${row["Figlio di"] || ""}</td>
                            <td class="px-6 py-4">${row.Eta || ""}</td>
                            <td class="px-6 py-4">${row["Professione/Grado di Parentela"] || ""}</td>
                            <td class="px-6 py-4">${row.Residenza || ""}</td>
                        `;
                        tbody.appendChild(tr);
                    });
                }
            });
        });
});