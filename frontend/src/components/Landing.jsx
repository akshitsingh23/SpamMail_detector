import React, { useState } from 'react';
import axios from 'axios';
import logo from '../192.jpg';
const Landing = () => {
    const [email, setEmail] = useState('');
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setResult('');
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', { email });
            console.log(response)
            setResult(response.data.result);
        } catch (error) {
            console.error("There was an error making the request:", error);
            setResult('Error');
        }
    };

    return (
        <div className='h-screen flex justify-center items-center '>
            <div className="flex items-center justify-between font-mono bg-white rounded-xl shadow-2xl shadow-white ">
                <div className="p-8 rounded-lg">
                    <div className='flex grid-cols-2 justify-center items-center'>
                        {/* <h2 className="text-4xl font-semibold mb-6 font-serif text-green-400 w-1/6">S</h2> */}
                        <div className='p-4'>
                        <img src={logo} className='p-10 rounded-full' width={200}></img>
                        </div>
                        <h2 className="text-4xl font-semibold mb-6 font-serif text-green-400">
                            <span style={{ color: 'red' }}>S</span>pam Mail Detector</h2>
                    </div>
                    <form onSubmit={handleSubmit} className='p-1'>
                        <textarea
                            className="w-full border border-green-500 border-2 text-xl  rounded mb-4 p-4  text-black"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Enter the email text here"
                        />
                        <button
                            type="submit"
                            className=" w-1/2 bg-blue-500 text-white py-2 rounded hover:bg-blue-600 duration-300 hover:text-black"
                        >Check for Spam</button>
                    </form>
                    {result && <p className="mt-4 text-lg font-semibold text-sky-500">Result: {result}</p>}
                </div>
            </div>
        </div>
    );
};

export default Landing;
