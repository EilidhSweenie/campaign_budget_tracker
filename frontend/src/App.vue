<script setup>
// Table items
  const items = [
    {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    },
        {
      name: 'Account A',
      budget: '£10000',
      spend: '£50',
      status: 'In Budget',
    },
    {
      name: 'Account B',
      budget: '£100',
      spend: '£50',
      status: 'Warning',
    },
    {
      name: 'Account C',
      budget: '£10',
      spend: '£50',
      status: 'Out of Budget',
    }
  ]

  // Define headers
  const headers =[
    { title: 'Name', key:'name', align:'start' },
    { title: 'Budget', key:'budget' },
    { title: 'Spend', key:'spend'  },
    { title: 'Status', key:'status', align:'end', sortable: true }
  ]

  // Add new campaign button functionality 
  const add = () =>{
    console.log('Add campaign clicked')
  }

  // Return expected colour based on status
  const getStatusColor = (status) => {
  switch (status) {
    case 'In Budget': return 'green'
    case 'Warning': return 'orange'
    case 'Out of Budget': return 'red'
    default: return 'grey'
  }
}
</script>

<template>
  <v-app>
    <v-main>
      <!-- Table Container -->
      <v-container fluid>
        <v-sheet border rounded>
          <v-data-table 
            :headers="headers"
            :items="items"
            >
            <!-- Table header with add campaign button -->
            <template v-slot:top>
              <v-toolbar flat color="primary">
                <!-- Title -->
                <v-toolbar-title>
                  Current Campaigns
                </v-toolbar-title>

                <!-- Button -->
                <v-btn
                  class="yellow-btn me-2"
                  rounded="lg"
                  prepend-icon="mdi-plus"
                  border
                  @click="add"
                >
                Add Campaign
                </v-btn>
              </v-toolbar>
            </template>
            
            <!-- Render status on traffic light system based on status -->
            <template v-slot:item.status="{ item }">
              <v-chip :color="getStatusColor(item.status)">
                {{ item.status }}
              </v-chip>
            </template>
          </v-data-table>
        </v-sheet>    
      </v-container>
    </v-main>
  </v-app>
</template>
  

<style>
  .yellow-btn {
    background-color: #FFDD33; 
  }
  .yellow-btn .v-btn__content,
  .yellow-btn .v-icon {
    color: #000 !important;
  }
</style>
