import React from 'react'
import {Link} from 'react-router-dom'

function Network() {
    return (
      <div className="Home">
        <header className="Home-header">
            <div>About the community</div>
            <Link to="/upload">Upload job</Link>
        </header>
      </div>
    );
  }

export default Network