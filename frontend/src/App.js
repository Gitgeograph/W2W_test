import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [items, setItems] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/tapp')
      .then(res => res.json())
      .then(
        (result) => {
          setItems(result);
        },
        
      )
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <div>
          {items.map(item => (
            <li key={item.id}>
              {item.text}
            </li>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
