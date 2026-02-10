import { useState } from "react";
import { UploadMindmap } from "./components/UploadMindmap";
import { MindmapViewer } from "./components/MindmapViewer";

export default function App() {
  const [mindmapId, setMindmapId] = useState<string | null>(null);

  return (
    <div>
      {!mindmapId && <UploadMindmap onOpen={setMindmapId} />}
      {mindmapId && <MindmapViewer id={mindmapId} />}
    </div>
  );
}
