document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("user-input");
    input.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userText = input.value.trim();
  if (!userText) return;

  chatBox.innerHTML += `<div><strong>Tú:</strong> ${userText}</div>`;

  const response = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userText })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;

  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}
