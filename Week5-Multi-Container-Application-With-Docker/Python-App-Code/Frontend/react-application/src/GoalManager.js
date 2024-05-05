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
      const response = await axios.get('https://your-api-url/goals');
      setGoalsList(response.data);
    } catch (error) {
      console.error('Error fetching goals:', error);
    }
  };

  const addGoal = async (newGoal) => {
    try {
      const response = await axios.post('https://your-api-url/goals', { title: newGoal });
      setGoalsList([...goalsList, response.data]);
    } catch (error) {
      console.error('Error adding goal:', error);
    }
  };

  const deleteGoal = async (id) => {
    try {
      await axios.delete(`https://your-api-url/goals/${id}`);
      setGoalsList(goalsList.filter((goal) => goal.id !== id));
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