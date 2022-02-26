import React from 'react'
import {Link} from 'react-router-dom'

function Jobs() {
    return (
      <div className="Jobs">
        <header className="Jobs-header">
            <Link to="/network">Network</Link>
            <div>Running job 1 ...</div>
            <div>Running job 2 ...</div>
        </header>
      </div>
    );
  }

export default Jobs