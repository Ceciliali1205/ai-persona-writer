window.onload = () => {
  const API_BASE = ""; // adjust if backend hosted elsewhere

  // Article generation
  const genBtn = document.getElementById("generate-btn");
  genBtn.onclick = async () => {
    const persona = document.getElementById("article-persona").value;
    const topic   = document.getElementById("article-topic").value.trim();
    if (!topic) return alert("Enter a topic");
    const res = await fetch(`${API_BASE}/generate_article`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ persona, topic })
    });
    const data = await res.json();
    document.getElementById("article-output").textContent = data.article || data.error;
  };

  // Comment generation
  const commentBtn = document.getElementById("comment-btn");
  commentBtn.onclick = async () => {
    const persona = document.getElementById("comment-persona").value;
    const article = document.getElementById("comment-article").value.trim();
    if (!article) return alert("Paste an article");
    const res = await fetch(`${API_BASE}/comment_article`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ persona, article })
    });
    const data = await res.json();
    document.getElementById("comment-output").textContent = data.comment || data.error;
  };
};