import { useState } from "react";
import { uploadMindmap } from "../api/mindmaps";

export function UploadMindmap({ onOpen }: { onOpen: (id: string) => void }) {
  const [file, setFile] = useState<File | null>(null);

  async function open() {
    if (!file) return;
    const res = await uploadMindmap(file);
    onOpen(res.id);
  }

  return (
    <div>
      <input
        type="file"
        accept=".mm"
        onChange={e => setFile(e.target.files?.[0] ?? null)}
      />
      <button onClick={open}>Open Mindmap</button>
    </div>
  );
}
