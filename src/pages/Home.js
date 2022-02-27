import React from 'react'
import {Link} from 'react-router-dom'
import './Home.scss'

function Home() {
    return (
      <body>
        <div className="container">
            <div className="container__item landing-page-container">
                <div className="content__wrapper">

                    {/* <header className="header">
                        <div className="menu-icon header__item">
                            <span className="menu-icon__line"></span>
                        </div>

                        <h1 className="heading header__item">D-UI</h1>

                        <ul className="social-container header__item">
                            <li className="social__icon social__icon--fb">
                                <img src="https://image.flaticon.com/icons/svg/1077/1077041.svg" alt="facebook"/>
                            </li>
                            <li className="social__icon social__icon--dr">
                                <img src="https://image.flaticon.com/icons/svg/25/25631.svg" alt="dribbble"/>
                            </li>
                            <li className="social__icon social__icon--in">
                                <img src="https://image.flaticon.com/icons/svg/1077/1077042.svg" alt="instagram"/>
                            </li>
                        </ul>
                    </header> */}

                    <p className="coords">N 51° 45' 38.268" /  W 1° 15' 45.7164"</p>

                    <div className="ellipses-container">

                        <div className="scrolling-words-container">
                            <div className="scrolling-words-box">
                                <ul>
                                <li>P2P</li>
                                <li>Distributed</li>
                                <li>Decentrelized</li>
                                <li>Secured</li>
                                <li>P2P</li>
                                </ul>
                            </div>
                        </div>
                        <h6 className="greeting">Arko</h6>

                        <div className="ellipses ellipses__outer--thin">

                            <div className="ellipses ellipses__orbit"></div>

                        </div>

                        <div className="ellipses ellipses__outer--thick"></div>
                    </div>

                    <div className="scroller">
                        <p className="page-title">
                        <Link to="/network">Join the Network</Link>
                        </p>

                        <div className="timeline">
                            <span className="timeline__unit"></span>
                            <span className="timeline__unit timeline__unit--active"></span>
                            <span className="timeline__unit"></span>
                        </div>
                    </div>
                </div>

            </div>

        </div>
      </body>
    );
  }

export default Home