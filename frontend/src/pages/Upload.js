import React from 'react'
import {Link} from 'react-router-dom'

function Upload() {
    return (
      <div className="Upload">
        <header className="Home-header">
            <div>Upload</div>
            <Link to="/jobs">See running jobs</Link>
        </header>
      </div>
    );
  }

export default Upload