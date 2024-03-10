#### In containers, we can categorize data in three categories

<ol>
<li>Read only data</li>
<ul>
<li>Code + Environment which we create for building images.</li>
<li>We do not want to change it after image is build.</li>
</ul>

<li>Temporary Application Data</li>
<ul>
<li>Data which we take or create when the container is running.</li>
<li>These are specific to that container.</li>
<li>Once the container is exited or deleted the data gets destroyed.</li>
<li>Ex: user inputs, temp DBS.</li>
</ul>


<li>Permanent Application Data</li>
<ul>
<li>We may need to create some data or take from outside and store them permanently.</li>
<li>They will be created when a container is running but should not get deleted when the container exits or restarts or gets deleted.</li>
<li>We need to create volumes that the containers will treat as DB.</li>
</ul>
</ol>