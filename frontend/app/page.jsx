'use client';

import * as React from 'react';
import {
  Box,
  Card,
  CardContent,
  CardMedia,
  Chip,
  Container,
  Grid,
  Stack,
  Typography
} from '@mui/material';

const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

export default function HomePage() {
  const [diseases, setDiseases] = React.useState([]);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    const load = async () => {
      try {
        const response = await fetch(`${apiBase}/diseases/`);
        if (!response.ok) {
          throw new Error('Unable to load diseases');
        }
        const data = await response.json();
        setDiseases(data);
      } catch (err) {
        setError(err.message);
      }
    };

    load();
  }, []);

  return (
    <Box sx={{ bgcolor: 'grey.50', minHeight: '100vh', py: 6 }}>
      <Container maxWidth="lg">
        <Stack spacing={1} sx={{ mb: 4 }}>
          <Typography variant="h3" component="h1">
            Medical Wiki
          </Typography>
          <Typography variant="body1" color="text.secondary">
            Browse diseases and their related symptoms, risk factors, and drugs.
          </Typography>
          <Stack direction="row" spacing={1}>
            <Chip label="Diseases" color="primary" />
            <Chip label="Symptoms" variant="outlined" />
            <Chip label="Risk Factors" variant="outlined" />
            <Chip label="Drugs" variant="outlined" />
          </Stack>
        </Stack>
        {error ? (
          <Typography color="error">{error}</Typography>
        ) : (
          <Grid container spacing={3}>
            {diseases.map((disease) => (
              <Grid item xs={12} md={6} key={disease.id}>
                <Card sx={{ display: 'flex', height: '100%' }}>
                  {disease.image ? (
                    <CardMedia
                      component="img"
                      sx={{ width: 180 }}
                      image={disease.image}
                      alt={disease.name}
                    />
                  ) : null}
                  <CardContent sx={{ flex: 1 }}>
                    <Typography variant="h5" component="h2">
                      {disease.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                      {disease.description || 'No description yet.'}
                    </Typography>
                    <Stack direction="row" spacing={1} sx={{ mt: 2, flexWrap: 'wrap' }}>
                      {disease.symptoms?.map((symptom) => (
                        <Chip key={`symptom-${symptom.id}`} label={symptom.name} size="small" />
                      ))}
                      {disease.risk_factors?.map((risk) => (
                        <Chip key={`risk-${risk.id}`} label={risk.name} size="small" color="secondary" />
                      ))}
                      {disease.drugs?.map((drug) => (
                        <Chip key={`drug-${drug.id}`} label={drug.name} size="small" variant="outlined" />
                      ))}
                    </Stack>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        )}
      </Container>
    </Box>
  );
}
