import React from 'react'
import {Link} from 'react-router-dom'

function Home() {
    return (
      <div className="Home">
        <header className="Home-header">
            <Link to="/network">Join network</Link>
        </header>
      </div>
    );
  }

export default Home