async function runPythonCode() {
    const code = document.getElementById("pythonCode").value;
    console.log("Sending code:", code);  // Log the code being sent to the server

    try {
        // Send the Python code to the server
        const response = await fetch('/run-python', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: code })
        });

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        // Parse the JSON response
        const result = await response.json();
        console.log("Received result:", result);  // Log the received result
        document.getElementById("output").innerText = result.output || "No output received.";
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("output").innerText = "Error: Unable to fetch or parse response.";
    }
}
