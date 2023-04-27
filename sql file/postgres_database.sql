
DROP TABLE IF EXISTS public.school_data;	
CREATE TABLE public.school_data
(
	Object_id character varying(100),
    school_name character varying(100),
	county character varying(100),
	latitude character varying(100) ,
	Longitude character varying(100)
);	

DROP TABLE IF EXISTS public.health_data;
CREATE TABLE public.health_data
(
	Object_id character varying(100),
	facility_name character varying(100),
    county character varying(100),
    latitude character varying(100),
    longitude character varying(100)
   );

ALTER TABLE IF EXISTS public.school_data
    OWNER to dap;
	
ALTER TABLE IF EXISTS public.health_data
    OWNER to dap;