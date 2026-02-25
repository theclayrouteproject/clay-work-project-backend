import React, { useEffect, useState } from 'react';

export default function PotteryList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const ac = new AbortController();

    const fetchPottery = async () => {
      try {
        const res = await fetch('https://clay-work-project-backend-production.up.railway.app/pottery', { signal: ac.signal });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setItems(data);
      } catch (err) {
        if (err.name === 'AbortError') return;
        console.error('Failed to fetch pottery items:', err);
      }
    };

    fetchPottery();
    return () => ac.abort();
  }, []);

  return (
    <section>
      <h2>Pottery</h2>
      <ul>
        {items.map((i) => (
          <li key={i.id}>{i.name} — ${i.price}</li>
        ))}
      </ul>
    </section>
  );
}
