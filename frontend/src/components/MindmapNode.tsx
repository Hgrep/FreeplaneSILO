export type Node = {
  id: string;
  text: string;
  children?: Node[];
};

export function MindmapNode({ node }: { node: Node }) {
  return (
    <div style={{ marginLeft: 20 }}>
      <div style={{ border: "1px solid #aaa", padding: 4 }}>
        {node.text}
      </div>

      {node.children?.map(child => (
        <MindmapNode key={child.id} node={child} />
      ))}
    </div>
  );
}
