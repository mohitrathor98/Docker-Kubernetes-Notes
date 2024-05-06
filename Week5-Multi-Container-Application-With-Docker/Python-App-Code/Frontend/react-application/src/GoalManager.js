import React, { useState, useEffect } from 'react';
import axios from 'axios';
import GoalForm from './GoalForm';
import GoalList from './GoalList';

function GoalManager() {
  const [goalsList, setGoalsList] = useState([]);

  useEffect(() => {
    fetchGoals();
  }, []);

  const fetchGoals = async () => {
    try {
      const response = await fetch('http://192.168.29.203:5000/view');
      const resData = await response.json();
      setGoalsList([...resData['goal']]);
    } catch (error) {
      console.error('Error fetching goals:', error);
    }
  };

  const addGoal = async (newGoal) => {
    try {
      const response = await axios.post('http://192.168.29.203:5000/store', { 'goal' : newGoal });
      console.log(response.data);
      fetchGoals()
    } catch (error) {
      console.error('Error adding goal:', error);
    }
  };

  const deleteGoal = async (goals) => {
    try {
      const response = await axios.post(`http://192.168.29.203:5000/delete`, {'goal': goals});
      console.log(response.data);
      fetchGoals()
    } catch (error) {
      console.error('Error deleting goal:', error);
    }
  };

  return (
    <div>
      <h2>Goal Manager</h2>
      <GoalForm onAddGoal={addGoal} /> <br/>
      <GoalList goals={goalsList} onDeleteGoal={deleteGoal} />
    </div>
  );
}

export default GoalManager;