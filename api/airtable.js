export default async function handler(req, res) {
  const PAT = process.env.AIRTABLE_PAT;
  const BASE_ID = process.env.AIRTABLE_BASE_ID;
  const TABLE_ID = process.env.AIRTABLE_TABLE_NAME;

  if (!PAT || !BASE_ID || !TABLE_ID) {
    return res.status(500).json({ error: 'Missing Airtable credentials in server environment.' });
  }

  try {
    let allRecordsCount = 0;
    let offset = null;
    let keepFetching = true;

    // Paginate through the Airtable view counting records. We ask for 0 fields to keep the data packet incredibly small.
    while (keepFetching) {
      const url = `https://api.airtable.com/v0/${BASE_ID}/${TABLE_ID}?maxRecords=100000&fields%5B%5D=Id` + 
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

      if (data.offset) {
        offset = data.offset;
      } else {
        keepFetching = false;
      }
    }

    return res.status(200).json({ 
       flightsLogged: allRecordsCount, 
       status: "success" 
    });

  } catch (e) {
     return res.status(500).json({ error: e.message });
  }
}
