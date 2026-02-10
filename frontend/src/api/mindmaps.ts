const API = "http://localhost:8000/api/v1";

export async function uploadMindmap(file: File) {
  const form = new FormData();
  form.append("file", file);

  const res = await fetch(`${API}/mindmaps/`, {
    method: "POST",
    body: form,
  });

  if (!res.ok) throw new Error("Upload failed");
  return res.json();
}

export async function getMindmapSession(id: string) {
  const res = await fetch(`${API}/mindmaps/${id}/session`);
  if (!res.ok) throw new Error("Not found");
  return res.json();
}
