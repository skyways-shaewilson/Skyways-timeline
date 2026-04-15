export default async function handler(req, res) {
  const PAT = process.env.AIRTABLE_PAT;
  const BASE_ID = process.env.AIRTABLE_BASE_ID;
  const TABLE_ID = process.env.AIRTABLE_TABLE_NAME;

  if (!PAT || !BASE_ID || !TABLE_ID) {
    return res.status(500).json({ error: 'Missing Airtable credentials in server environment.' });
  }

  try {
    let allRecordsCount = 0;
    let globalLifetimeFlights = 0;
    let totalFlightHours = 0;
    let totalDistanceKm = 0;
    
    let offset = null;
    let keepFetching = true;

    // Paginate through the Airtable view counting records and aggregating stats.
    while (keepFetching) {
      const url = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}?fields%5B%5D=Flight%20%23&fields%5B%5D=Flight%20time%20(h)&fields%5B%5D=Dist%20Cruise%20(km)` + 
                  (offset ? `&offset=${offset}` : '');
                  
      const response = await fetch(url, {
        headers: {
          'Authorization': `Bearer ${PAT}`
        }
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(`Airtable API error: ${JSON.stringify(errData)}`);
      }

      const data = await response.json();
      allRecordsCount += (data.records || []).length;
      
      (data.records || []).forEach(record => {
        const fNum = record.fields['Flight #'] || 0;
        if (fNum > globalLifetimeFlights) globalLifetimeFlights = fNum;
        
        totalFlightHours += (record.fields['Flight time (h)'] || 0);
        totalDistanceKm += (record.fields['Dist Cruise (km)'] || 0);
      });

      if (data.offset) {
        offset = data.offset;
      } else {
        keepFetching = false;
      }
    }

    return res.status(200).json({ 
       globalFlights: globalLifetimeFlights,
       activeFlights: allRecordsCount,
       flightHours: Math.round(totalFlightHours),
       distanceKm: Math.round(totalDistanceKm),
       status: "success" 
    });

  } catch (e) {
     return res.status(500).json({ error: e.message });
  }
}
