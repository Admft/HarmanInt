import React from 'react';
import '../styles/Home.css';
import harmanLogo from '../assets/Harmanlogopng.png';
import speakerImage from '../assets/HKcarspeaker.jpg';
import doorSpeakerImage from '../assets/Doorspeaker.jpg';
import doorSpeakerRedImage from '../assets/DoorSpeakerRed.jpeg';
import twoSpeakersImage from '../assets/TwoSpeakers.jpeg';

function Home() {
    return (
        <div className="home-container">
            <header className="home-header">
                <img src={harmanLogo} alt="Harman Logo" className="home-logo" />
                <div className="nav-container">
                    <nav className="home-navigation">
                        <a href="/products" className="nav-link">Products</a>
                        <a href="/about" className="nav-link">About</a>
                        <a href="/support" className="nav-link">Support</a>
                    </nav>
                    {/* Wrap Logout button with a link */}
                    <a href="/login" className="logout-button-link">
                        <button className="logout-button">Logout</button>
                    </a>
                </div>
            </header>


            <main className="home-main">
            <section className="hero-section">
    <div className="hero-text">
        <h1>Immersive Acoustic Elegance</h1>
        <p className="hero-subtext">Experience Sound Differently</p>
    </div>
    {/* Removed the img tag from here */}
</section>

                <section className="product-launch">
                    <img src={doorSpeakerImage} alt="Harman Kardon Door Speaker" className="product-image left" />
                    <div className="launch-details">
                        <h2>Harman Kardon Door Speakers: A Symphony on Wheels</h2>
                        <p>Introducing a symphony on wheels with our Harmonic Series. Discover the relentless pursuit of acoustic perfection, now embodied in your vehicle's sanctuary.</p>
                    </div>
                    <img src={doorSpeakerRedImage} alt="Harman Kardon Door Speaker Red" className="product-image right" />
                </section>

                <section className="aftermarket-product-section">
                    <div className="technology-details">
                        <h2>Upgrade to Excellence</h2>
                        <p>If your car didn't come with a Harman Kardon system, elevate your experience with our superior door speakers.</p>
                    </div>
                    <div className="speaker-image-wrapper">
                        <img src={speakerImage} alt="Harman Kardon Speaker" className="speaker-image" />
                    </div>
                </section>

                <section className="final-impressions-section">
                    <div className="vision-text">
                        <h2>Our Vision: Your Soundtrack</h2>
                        <p>At Harman Kardon, we blend innovation with art to create your personal soundtrack.</p>
                    </div>
                </section>
            </main>

            <footer className="home-footer">
                <p>Harman Kardon. The Art of Sound.</p>
            </footer>
        </div>
    );
}

export default Home;
