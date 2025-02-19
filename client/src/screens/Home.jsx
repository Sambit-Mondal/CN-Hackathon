import { useState, useContext } from 'react';
import Navbar from '../components/Navbar';
import ResourceTrading from '../components/ResourceTrading';
import { AuthContext } from '../contexts/AuthContextFile';
import QrModal from '../components/QrModal';

const Home = () => {
    const [activeView, setActiveView] = useState('resourceTrading');
    const { store } = useContext(AuthContext);

    // QR Modal state moved here
    const [qrCode, setQrCode] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);

    // Show loading screen while fetching store details
    if (!store) {
        return (
            <div className="w-full h-screen flex items-center justify-center">
                <h1 className="text-white text-lg">Loading...</h1>
            </div>
        );
    }

    return (
        <div className="w-full h-screen bg-mlsa-bg flex items-center justify-between px-5">
            <Navbar
                setActiveView={setActiveView}
                activeView={activeView}
                setQrCode={setQrCode} // Pass down state
                setIsModalOpen={setIsModalOpen}
            />
            {activeView === 'resourceTrading' ? <ResourceTrading /> : null}

            {/* QR Modal outside Navbar, inside Home */}
            <QrModal qrCode={qrCode} isModalOpen={isModalOpen} setIsModalOpen={setIsModalOpen} />
        </div>
    );
};

export default Home;