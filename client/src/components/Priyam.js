import React from 'react';
import Alex from './Alex';
import './test.css';

const priyamDetails = {
  name: 'Priyam',
  age: 20,
  height: '180cm'
};

function Priyam() {
  return (
    <div>
      Hi
      <p className='hello'>I'm {priyamDetails.name}</p>
      <p>I'm {priyamDetails.age} years old</p>
      <p>My height is {priyamDetails.height}</p>
      <p>Family info</p>
      <Alex baapKaData={priyamDetails} />
    </div>
  );
}

export default Priyam;
