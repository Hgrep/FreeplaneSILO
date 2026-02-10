import { useEffect, useState } from "react";
import { getMindmapSession } from "../api/mindmaps";
import { MindmapNode } from "./MindmapNode";
import type { Node } from "./MindmapNode"; //type-only import

export function MindmapViewer({ id }: { id: string }) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    getMindmapSession(id).then(setData);
  }, [id]);

  if (!data) return <div>Loading…</div>;

  return (
    <div>
      <h2>{data.title}</h2>
      <MindmapNode node={data.root as Node} />
    </div>
  );
}
