import * as React from 'react';
import { Link } from "react-router-dom"
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import RestoreIcon from '@mui/icons-material/Restore';
import FavoriteIcon from '@mui/icons-material/Favorite';
import LocationOnIcon from '@mui/icons-material/LocationOn';

const Navigation2 = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      > 
        <BottomNavigationAction label="Home" icon={<Link to = "/home"><RestoreIcon /></Link>} />
        <BottomNavigationAction label="Counter" icon={<Link to = "/counter"><FavoriteIcon /></Link>} />
        <BottomNavigationAction label="Todos" icon={<Link to = "/todos"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="Signup" icon={<Link to = "/auth/signup"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="Login" icon={<Link to = "/auth/login"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="User-List" icon={<Link to = "/auth/userlist"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="뇌졸중" icon={<Link to = "/stroke"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="iris" icon={<Link to = "/iris"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="number" icon={<Link to = "/number"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="navermovie" icon={<Link to = "/navermovie"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="samsung" icon={<Link to = "/nlp/samsung-report"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="naver-review" icon={<Link to = "/nlp/imdb"><LocationOnIcon /></Link>} />
        <BottomNavigationAction label="korean-classify" icon={<Link to = "/nlp/korean-classify"><LocationOnIcon /></Link>} />
      </BottomNavigation>
    </Box>
  );
}

export default Navigation2
